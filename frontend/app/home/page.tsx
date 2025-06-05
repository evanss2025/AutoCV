'use client';

import { useEffect, useState } from "react";

export default function Home() {

  // const [message, setMessage] = useState("loading");

  // useEffect(() => {
  //   fetch("http://localhost:8080/").then(
  //     response => response.json()
  //   ).then(
  //     data => {
  //       console.log(data);
  //       setMessage(data.message);
  //     }
  //   )

  // }, [])

  return (
    <div className="flex flex-col justify-center items-center min-h-screen w-1/4">
      <h1>Your Resumes:</h1>
      {/* <h2>Your LinkedIn profile is {{ messages:['link'] }}</h2> */}

      
    </div>
  );
}
