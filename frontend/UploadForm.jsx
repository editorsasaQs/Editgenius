import React, { useState } from "react";

const UploadForm = () => {
  const [format, setFormat] = useState("youtube");

  return (
    <div className="bg-[#1a1a1a] p-6 rounded-md shadow-lg mt-6">
      <h2 className="text-xl font-semibold mb-4">Upload Your Media</h2>

      <form className="flex flex-col gap-4">
        <input type="file" accept="video/*" className="bg-black p-2 rounded" />
        <input type="file" accept="audio/*" className="bg-black p-2 rounded" />
        <input type="file" accept="audio/*" className="bg-black p-2 rounded" />
        <input type="file" accept="image/*" className="bg-black p-2 rounded" />

        <select
          value={format}
          onChange={(e) => setFormat(e.target.value)}
          className="bg-black p-2 rounded"
        >
          <option value="youtube">YouTube Format (16:9)</option>
          <option value="reel">Reel Format (9:16)</option>
        </select>

        <button
          type="submit"
          className="bg-primary text-black font-bold py-2 rounded hover:bg-green-600 transition"
        >
          Upload & Process
        </button>
      </form>
    </div>
  );
};

export default UploadForm;
