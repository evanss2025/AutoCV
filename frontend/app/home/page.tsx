'use client';

import { useEffect, useState } from "react";
import Resume from '../../components/resume';
import { useRouter } from "next/navigation";

export default function Home() {
    const [contact, setContact] = useState("Loading...");
    const [name, setName] = useState("Loading...");
    const router = useRouter();

    useEffect(() => {
    
      fetch('http://localhost:8080/home').then(
        response => response.json()
      ) .then(data => {
          setContact(data.contact)
          setName(data.name)
    })
    .catch(error => {
      // 4. If there’s an error (like server isn’t running), show a message
      setContact("Can't find contact")
    });

    
    }, []);

    const goBack = () => {
      router.push('/submit')
    }

  return (
    <div className="flex flex-col items-center min-h-screen mt-5 w-10/12">
      <div id="go-back" className="text-4xl font-bold absolute left-10">
        <button onClick={goBack}>&larr;</button>
      </div>
      <h1 className="text-3xl p-3rounded-xl m-3">Your Resumes:</h1>
      <h1>{contact}</h1>
      <h1>{name}</h1>
      <div className="mt-5 grid grid-rows-2 grid-cols-4 w-full items-center gap-5" id='resumes'>
        <Resume 
          name="Original Resume"
        />
        <Resume
          name="Ivy League"
        />
        <Resume
          name="Stylish"
        />
        <Resume
          name="Single Column"
        />
        <Resume
          name="Double Column"
        />
        <Resume
          name="Classic"
        />
      </div>
    </div>
  );
}
