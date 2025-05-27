export default function Home() {
  return (
    <div className="flex flex-col justify-center items-center min-h-screen">
      <h1 className="text-6xl font-bold m-6">AutoCV</h1>
      <h3 className="text-lg">Upload your LinkedIn data below</h3>

      <div id="file_upload" className="m-5">
        <input
          type="file"
          id="fileUpload"
          className="hidden"
        />
        <label
          htmlFor="fileUpload"
          className="bg-gray-200 text-black px-4 py-2 rounded-lg cursor-pointer hover:bg-gray-300 transition"
        >
          Choose File
        </label>
      </div>
      <button className="transition duration-200 bg-blue-600 text-white p-3 rounded-xl hover:bg-blue-800 text-2xl m-5">Create CV!</button>
    </div>
  );
}
