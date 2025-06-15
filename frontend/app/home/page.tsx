'use client';

import { useEffect, useState } from "react";
import Resume from '../../components/resume';
import { useRouter } from "next/navigation";

export default function Home() {
    const [name, setName] = useState("Loading...");
    const router = useRouter();

    useEffect(() => {
    
      fetch('http://localhost:8080/home').then(
        response => response.json()
      ) .then(data => {
          setName(data.name.trim())
    })
    .catch(error => {
      // 4. If there’s an error (like server isn’t running), show a message
      setName("Can't find name")
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
      <h1 className="text-3xl p-3rounded-xl m-3">Hi, {name}, here are your resumes:</h1>
      <div className="mt-5 grid grid-rows-2 grid-cols-4 w-full items-center gap-5" id='resumes'>
        <Resume
          image="public/ivy_league_example.png"
          name="Original Resume"
        />
        <Resume
          image="public/ivy_league_example.png"
          name="Ivy League"
        />
        <Resume
          image="public/stylish_example.jpg"
          name="Stylish"
        />
        <Resume
          image="public/single_column_example.png"
          name="Single Column"
        />
        <Resume
          image="public/double_column_example.png"
          name="Double Column"
        />
        <Resume
          image="public/classic_example.png"
          name="Classic"
        />
      </div>
    </div>
  );
}
