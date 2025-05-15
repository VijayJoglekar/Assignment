import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Line } from 'react-chartjs-2';
import 'chart.js/auto'; 

function LocationAnalyzer() {
  const [locationData, setLocationData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [location, setLocation] = useState('Wakad');

  const fetchData = async (loc) => {
    try {
      setLoading(true);
      const response = await axios.get(`http://localhost:8000/api/analyze/${loc}`);
      setLocationData(response.data);
    } catch (error) {
      console.error("Error fetching data:", error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData(location);
  }, [location]);

  if (loading) return <div className="loading">Loading data...</div>;


  const priceChartData = {
    labels: locationData.data.map(item => item.year),
    datasets: [
      {
        label: 'Flat Average Price (₹/sqft)',
        data: locationData.data.map(item => item.flat_avg_price),
        borderColor: 'rgb(75, 192, 192)',
        tension: 0.1
      }
    ]
  };

  return (
    <div className="analysis-container">
      <h1>Real Estate Analysis: {locationData.location}</h1>
      
      <div className="search-box">
        <input 
          type="text" 
          value={location}
          onChange={(e) => setLocation(e.target.value)}
          placeholder="Enter location (e.g. Wakad)"
        />
        <button onClick={() => fetchData(location)}>Analyze</button>
      </div>

      <div className="chart-container">
        <h2>Price Trends (2020-2024)</h2>
        <Line data={priceChartData} />
      </div>

      <div className="data-table">
        <h2>Detailed Statistics</h2>
        <table>
          <thead>
            <tr>
              <th>Year</th>
              <th>Total Sales (₹)</th>
              <th>Units Sold</th>
              <th>Avg Flat Price (₹/sqft)</th>
            </tr>
          </thead>
          <tbody>
            {locationData.data.map(item => (
              <tr key={item.id}>
                <td>{item.year}</td>
                <td>{item.total_sales.toLocaleString('en-IN')}</td>
                <td>{item.total_sold.toLocaleString()}</td>
                <td>{item.flat_avg_price.toFixed(2)}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default LocationAnalyzer;