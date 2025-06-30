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
    <div className="flex flex-col justify-center items-center min-h-screen w-10/12">
      <div id="go-back" className="text-4xl font-bold absolute left-14 top-4">
        <button onClick={goBack}>&larr;</button>
      </div>
      <h1 className="text-3xl p-3 rounded-xl m-3 mt-6">Hi, {name}, here are your resumes:</h1>
      <div className="mt-5 grid auto-rows-fr grid-cols-1 md:grid-cols-2 w-2/3 items-center gap-5" id='resumes'>
        <Resume
          image="/example_images/ivy_league_example.png"
          name="Ivy League"
        />
        <Resume
          image="/example_images/single_column_example.png"
          name="Single Column"
        />
        {/* <Resume
          image="/example_images/classic_example.png"
          name="Classic"
        /> */}
      </div>
    </div>
  );
}
