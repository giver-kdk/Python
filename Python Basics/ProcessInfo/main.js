// ***** For now, this code works for windows only. Can easily be made cross-platform ***** 
const pidusage = require('pidusage');
const si = require('systeminformation');
const fs = require('fs');
const os = require('os');

// Method to find locally running react app's process ID
async function findReactAppPid() {
  const processList = await si.processes();
  const myReactApp = processList.list.find(
    (p) => p.name === 'node.exe' && p.command.includes('react-scripts')				// Get the process via 'name'
  );
  return myReactApp ? myReactApp.pid : null;										// Indicate if process found or not
}

// Method to constantly monitor the locally running react app
async function monitorReactApp(pid, duration = 60, interval = 1000) {
  const startTime = Date.now();
  const infoOutputFile = fs.createWriteStream('react_app_monitoring.csv');
  infoOutputFile.write('Time\t\t\t\t|\tCPU(%)\t|Memory Usage(MB)|Data Sent(MB)|Data Received(MB)\n');

  console.log('Monitoring React App...');
  console.log('Time\t\t\t\t|\tCPU(%)\t|Memory Usage(MB)|Data Sent(MB)|Data Received(MB)');

  const initialNetIO = await si.networkStats();
  const initialBytesSent = initialNetIO[0].tx_bytes;
  const initialBytesReceived = initialNetIO[0].rx_bytes;

  const intervalId = setInterval(async () => {
	// Stop if the duration of reached
    if (Date.now() - startTime > duration * 1000) {
      clearInterval(intervalId);
      infoOutputFile.end();
      console.log('Monitoring finished.');
      return;
    }
	// Else continue printing stats
    try {
      const stats = await pidusage(pid);
      const netIO = await si.networkStats();

      const cpuUsage = stats.cpu.toFixed(2);
      const memoryUsage = (stats.memory / (1024 * 1024)).toFixed(2); 					// Memory used in MB
      const dataSent = ((netIO[0].tx_bytes - initialBytesSent) / (1024 * 1024)).toFixed(2); // Data sent in MB
      const dataReceived = ((netIO[0].rx_bytes - initialBytesReceived) / (1024 * 1024)).toFixed(2); // Data received in MB

      const timestamp = new Date().toLocaleTimeString();
	//   Write the stats in the output file
      infoOutputFile.write(`${timestamp}\t|\t${cpuUsage}\t|\t${memoryUsage}\t|\t${dataSent}\t|\t${dataReceived}\n`);

      console.log(`${timestamp}\t|\t${cpuUsage}\t|\t${memoryUsage}\t|\t${dataSent}\t|\t${dataReceived}`);
    } catch (err) {
      console.error('Error monitoring the local react app:', err.message);
      clearInterval(intervalId);
      infoOutputFile.end();
    }
  }, interval);
}

// Entry point of the program
async function main() {
  const pid = await findReactAppPid();
  if (pid) {
    console.log(`Local react app PID: ${pid}`);
	// Monitor for 2 minutes, log every 3 seconds
    monitorReactApp(pid, 120, 3000);  
  } else {
    console.error('No local react app found.');
  }
};
main();
