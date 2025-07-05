import React from "react";
import Header from "./components/Header";
import UploadForm from "./components/UploadForm";
import StatusCard from "./components/StatusCard";

const App = () => {
  return (
    <div className="min-h-screen bg-dark text-white font-sans">
      <Header />
      <main className="max-w-4xl mx-auto px-4 py-6">
        <UploadForm />
        <StatusCard />
      </main>
    </div>
  );
};

export default App;
