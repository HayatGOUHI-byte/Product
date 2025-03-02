// Dashboard.js
import React from 'react';
import './Dashboard.css';

import { FaSearch } from 'react-icons/fa';

const Dashboard = () => {
  return (
    <div className="flex h-screen bg-gray-100">
      {/* Sidebar */}
      <aside className="w-64 bg-gray-900 text-white flex flex-col">
        <div className="p-4 font-bold text-xl">AHDIGITAL</div>
        <nav className="flex-1">
          {['Launchpad', 'Dashboard', 'Conversations', 'Calendars', 'Contacts', 'Opportunities', 'Payments', 'Marketing', 'Automation', 'Sites', 'Memberships', 'Settings'].map((item) => (
            <a key={item} href="#" className="block py-2.5 px-4 hover:bg-gray-700">{item}</a>
          ))}
        </nav>
      </aside>

      {/* Main Content */}
      <div className="flex-1 overflow-y-auto p-6">
        {/* Header */}
        <div className="flex justify-between items-center mb-6">
          <h1 className="text-2xl font-bold">Dashboard</h1>
          <input type="date" className="border p-2 rounded" />
        </div>

        {/* Cards Container */}
        <div className="grid grid-cols-3 gap-4">
          <DashboardCard title="Opportunity Status" />
          <DashboardCard title="Opportunity Value" />
          <ConversionRateCard />
        </div>

        {/* Lower Section */}
        <div className="grid grid-cols-2 gap-4 mt-6">
          <DashboardCard title="Funnel" dropdown />
          <DashboardCard title="Stage Distribution" dropdown />
        </div>
      </div>
    </div>
  );
};

const DashboardCard = ({ title, dropdown }) => (
  <div className="bg-white p-4 rounded-lg shadow">
    <div className="flex justify-between items-center">
      <h2 className="font-semibold">{title}</h2>
      {dropdown && <select className="text-sm border rounded p-1"><option>No pipeline available</option></select>}
    </div>
    <div className="flex flex-col items-center justify-center h-40 text-gray-500">
      <FaSearch className="text-blue-400 text-3xl mb-2" />
      <p>No Data Found</p>
    </div>
  </div>
);

const ConversionRateCard = () => (
  <div className="bg-white p-4 rounded-lg shadow">
    <h2 className="font-semibold">Conversion Rate</h2>
    <div className="flex flex-col items-center justify-center h-40">
      <div className="text-3xl font-bold">MADO</div>
      <div className="text-green-500 text-sm">↑ 0% vs Last 31 Days</div>
      <div className="relative w-24 h-24 mt-2">
        {/* Cercle Placeholder */}
        <svg className="w-full h-full" viewBox="0 0 100 100">
          <circle cx="50" cy="50" r="45" stroke="#E5E7EB" strokeWidth="8" fill="none" />
          <circle cx="50" cy="50" r="45" stroke="#3B82F6" strokeWidth="8" fill="none" strokeDasharray="283" strokeDashoffset="283" />
        </svg>
        <div className="absolute inset-0 flex items-center justify-center text-xl font-bold">0%</div>
      </div>
      <p className="text-gray-500 mt-1">Won revenue</p>
      <p className="text-xl font-bold">MAD0</p>
    </div>
  </div>
);

export default Dashboard;
