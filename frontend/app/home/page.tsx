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
      <div id="go-back" className="text-4xl font-bold absolute left-14">
        <button onClick={goBack}>&larr;</button>
      </div>
      <h1 className="text-3xl p-3rounded-xl m-3">Hi, {name}, here are your resumes:</h1>
      <div className="mt-5 grid grid-rows-2 grid-cols-4 w-full items-center gap-5" id='resumes'>
        <Resume
          image="/example_images/google_example.png"
          name="Google Resume"
        />
        <Resume
          image="/example_images/ivy_league_example.png"
          name="Ivy League"
        />
        <Resume
          image="/example_images/stylish_example.jpg"
          name="Stylish"
        />
        <Resume
          image="/example_images/single_column_example.png"
          name="Single Column"
        />
        <Resume
          image="/example_images/double_column_example.png"
          name="Double Column"
        />
        <Resume
          image="/example_images/classic_example.png"
          name="Classic"
        />
      </div>
    </div>
  );
}
