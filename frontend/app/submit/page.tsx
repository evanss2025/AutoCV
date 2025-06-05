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
      {/* <h3>{message}</h3> */}
      <h1 className="text-6xl font-bold m-6">AutoCV</h1>
      <h3 className="text-lg">Link your LinkedIn profile below</h3>

      <form 
        className="m-5 w-full items-center flex flex-col justify-center"
        method="post"
        action="http://localhost:8080/submit">
          <input
            type="text"
            id="link_input"
            name="link"
            className="bg-stone-200 p-3 rounded-xl w-full"
          />
        <input type="submit"  value='Create CV!' className="transition duration-200 bg-blue-600 text-white p-3 rounded-xl hover:bg-blue-800 text-2xl m-5"></input>
      </form>

      
    </div>
  );
}
