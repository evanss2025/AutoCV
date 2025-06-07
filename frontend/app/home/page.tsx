'use client';

import { useEffect, useState } from "react";
import Resume from '../../components/resume';


export default function Home() {
    const [name, setName] = useState("Loading...");

    useEffect(() => {

    const params = new URLSearchParams(window.location.search);
    const link = params.get("lnk");        
    
    if (link) {
        fetch(`http://localhost:8080/home?lnk=${encodeURIComponent(link)}`).then(
            response => response.json()
            ).then(
            data => {
                console.log(data);
                setName(data.name);
            }
        )
    } else {
        setName("Can't find link")
    }
    
    }, []);

  return (
    <div className="flex flex-col items-center min-h-screen mt-5 w-10/12">
      <h1 className="text-2xl bg-blue-600 p-3 text-white rounded-xl">Your Resumes:</h1>
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
