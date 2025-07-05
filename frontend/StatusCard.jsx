import React from "react";

const StatusCard = () => {
  return (
    <div className="bg-[#1f1f1f] mt-8 p-4 rounded shadow-lg">
      <h3 className="text-lg font-semibold">Processing Status</h3>
      <p className="text-sm text-gray-400">No uploads yet.</p>
    </div>
  );
};

export default StatusCard;
