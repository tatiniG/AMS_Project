async function fetchData() {
    const patientsRes = await fetch('/api/patients');
    const patients = await patientsRes.json();
    populateTable('Patients', patients);
  
    const locationRes = await fetch('/api/locations');
    const locations = await locationRes.json();
    populateTable('Locations', locations);
  }
  
  function populateTable(id, data) {
    const table = document.getElementById(id);
    if (data.length === 0) {
      table.innerHTML = '<tr><td>No data available</td></tr>';
      return;
    }
    const headers = Object.keys(data[0]);
    table.innerHTML = `
      <tr>${headers.map(h => `<th>${h}</th>`).join('')}</tr>
      ${data.map(row => `<tr>${headers.map(h => `<td>${row[h]}</td>`).join('')}</tr>`).join('')}
    `;
  }
  #fetch
  fetchData();
  
