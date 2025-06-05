'use client';

import { useEffect, useState } from "react";

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
    <div className="flex flex-col justify-center items-center min-h-screen w-1/4">
      <h1>{name}</h1>
    </div>
  );
}
