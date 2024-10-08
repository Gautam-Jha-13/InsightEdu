import React, { useState } from "react";

const FileUpload = () => {
  const [files, setFiles] = useState(null);

  const handleFileChange = (event) => {
    setFiles(event.target.files);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    if (files) {
      console.log("Uploading files:", files);
    } else {
      alert("No files selected");
    }
  };

  return (
    <div className="file-upload">
      <h3>Upload Your Files and Type:</h3>
      <input type="file" multiple onChange={handleFileChange} />
      <button className="submit-button" onClick={handleSubmit}>✔️</button>
      <button className="cancel-button" onClick={() => setFiles(null)}>❌</button>
    </div>
  );
};

export default FileUpload;
