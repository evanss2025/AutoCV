'use client';

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

export default function Home() {
  
  const router = useRouter();
  const [file, setFile] = useState("No File Selected")
  const [loading, setLoading] = useState(false);

  const handleUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const input = e.target;
    if (input && input.files && input.files.length > 0) {
      setFile(input.files[0].name);
    }
  }

  const handleFormSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setLoading(true);

    const form = e.currentTarget;
    const formData = new FormData(form);
    const submitButton = document.getElementById('submit');

    if (loading && submitButton) {
      submitButton.classList.add('animate-spin')
    }

    const res = await fetch("http://localhost:8080/submit", {
      method: "POST",
      body: formData,
    });

    if (res.ok) {
      router.push("/home"); // redirect to home  if upload is successful
    } else {
      alert("Upload failed");
    }
    setLoading(false);
  };

  return (
    <div className="flex flex-col justify-center items-center min-h-screen w-1/4">
      {/* <h3>{message}</h3> */}
      <h1 className="text-6xl font-bold m-6">AutoCV</h1>
      <h3 className="text-lg">Upload your LinkedIn data below:</h3>

      <div className="flex flex-col items-center justify-center">

        <form 
          className="m-5 w-full items-center flex flex-col justify-center text-center"
          onSubmit={handleFormSubmit}
        >
            <label
              htmlFor="link_input"
              className="cursor-pointer px-4 py-2 bg-gray-200 rounded-lg text-center hover:bg-gray-300"
            >
              Upload Linkedin Data
            </label>
            <input
              type="file"
              id="link_input"
              name="file"
              className="hidden"
              onChange={handleUpload}
              required
            />
            <h2 id="file" className="m-2">{file}</h2>
          <input id="submit" type="submit"  value={loading ? "Uploading Resume..." : "Create CV!"} className="cursor-pointer transition duration-200 bg-blue-600 text-white p-3 rounded-xl hover:bg-blue-800 text-2xl m-3"></input>
        </form>
      </div>
    </div>
  );
}
