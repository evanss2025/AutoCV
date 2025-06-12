'use client';

import { useEffect, useState } from "react";
import Resume from '../../components/resume';


export default function Home() {
    const [contact, setContact] = useState("Loading...");

    useEffect(() => {
    
      fetch('http://localhost:8080/home').then(
        response => response.json()
      ) .then(data => {
          setContact(data.contact)
    })
    .catch(error => {
      // 4. If there’s an error (like server isn’t running), show a message
      setContact("Can't find contact")
    });

    
    }, []);

  return (
    <div className="flex flex-col items-center min-h-screen mt-5 w-10/12">
      <h1 className="text-3xl p-3rounded-xl m-3">Your Resumes:</h1>
      <h1>{contact}</h1>
      <div className="mt-5 grid grid-rows-2 grid-cols-4 w-full items-center gap-5" id='resumes'>
        <Resume 
          name="resume 1"
        />
        <Resume
          name="resume 2"
        />
        <Resume
          name="resume 3"
        />
        <Resume
          name="resume 4"
        />
        <Resume
          name="resume 5"
        />
        <Resume
          name="resume 6"
        />
      </div>
    </div>
  );
}
