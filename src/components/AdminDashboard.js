import React from "react";
import FileUpload from "./FileUpload";
import Sidebar from "./Sidebar";
import DatabaseSelector from "./DatabaseSelector";

const AdminDashboard = () => {
  return (
    <div className="admin-dashboard">
      <Sidebar />
      <div className="dashboard-content">
        <section className="media-section">
          <h2>Section 8</h2>
          <div className="media-options">
            <div className="media-item">Presentation</div>
            <div className="media-item">Document</div>
            <div className="media-item">White Boards</div>
            <div className="media-item">Forms / Surveys</div>
            <div className="media-item">Charts / Graphs</div>
            <div className="media-item">Infographics</div>
            <div className="media-item">Videos / GIFs</div>
            <div className="media-item">Printables</div>
          </div>
        </section>

        <DatabaseSelector />
        <FileUpload />
      </div>
    </div>
  );
};

export default AdminDashboard;
