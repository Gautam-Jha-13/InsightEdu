import React from "react";

const DatabaseSelector = () => {
  return (
    <div className="database-selector">
      <label htmlFor="database">Select Your Database</label>
      <select id="database">
        <option value="db1">Database 1</option>
        <option value="db2">Database 2</option>
      </select>
      <button className="manual-entry">Manually</button>
    </div>
  );
};

export default DatabaseSelector;
