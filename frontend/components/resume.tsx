import React from 'react'

function Resume({name}: {name: String}) {
  return (
    <div className='flex items-center justify-center flex-col m-6'>
        <div className='p-5 shadow-lg rounded-xl outline-2 outline-blue-600 w-full flex flex-col items-center justify-center'>
            <div id='placeholder-image' className='bg-slate-300 p-5 m-2'>placeholder image</div>
            <h1>{name}</h1>
        </div>
        <button className='text-lg w-full outline-blue-600 p-2 rounded-xl mt-5 outline-2 hover:bg-stone-100 transition duration-200'>View</button>
        <button className='text-lg w-full bg-blue-600 p-2 text-white rounded-xl mt-5 hover:bg-blue-800 transition duration-200'>Download</button>
        
    </div>
  )
}

export default Resume