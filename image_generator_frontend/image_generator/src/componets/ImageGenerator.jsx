// import React, { useState } from 'react';
// import { apiServices } from '../api/UsersApi';

// const ImageGenerator = () => {
//     const [inputText, setInputText] = useState('');
//     const [generatedImage, setGeneratedImage] = useState(null);

//     const handleInputChange = (e) => {
//         setInputText(e.target.value);
//     };

//     const handleGenerateImage = async () => {
//         // const image = generateImageFromText(inputText);
//         const response = await apiServices.generateImage({"prompt":inputText})
//         console.log("This is the response i have ::---", response)
//         if(response){
//             setGeneratedImage(response?.data)
//         }
//         // setGeneratedImage(image);
//     };

//     console.log(generatedImage)

//     const handleDownloadImage = () => {
//         downloadImage(generatedImage);
//     };

//     return (
//         <section className='w-full h-full p-14  flex justify-center items-center'>

//             <div className="container mx-auto   p-16">
//                 <div className='flex justify-center h-80 shadow-lg'>
//                     {generatedImage ? (
//                         <>
//                             <img src={generatedImage} alt="Generated Image" className="max-w-full mb-4" />
//                             <button onClick={handleDownloadImage} className="bg-green-500 text-white px-4 py-2 rounded">Download Image</button>
//                         </>
//                     ) : (
//                         <img src="https://images.nightcafe.studio/jobs/ogBIc50pY1WVacF3L8zM/ogBIc50pY1WVacF3L8zM.jpg?tr=w-1600,c-at_max" alt="Dummy Image" className="max-w-full mb-4" />
//                     )}
//                 </div>
//                 <input
//                     type="text"
//                     value={inputText}
//                     onChange={handleInputChange}
//                     placeholder="Enter text..."
//                     className="border border-gray-400 p-2 mb-4 w-full"
//                 />
//                 <button onClick={handleGenerateImage} className="bg-red-500 text-white px-4 py-2 rounded mr-4">Generate Image</button>
//                 <button onClick={handleGenerateImage} className="bg-yellow-500 text-white px-4 py-2 rounded mr-4">Downlod Image</button>
//             </div>
//         </section>
//     );
// };

// export default ImageGenerator;

import React, { useState } from 'react';
import { apiServices } from '../api/UsersApi';

const ImageGenerator = () => {
    const [inputText, setInputText] = useState('');
    const [generatedImage, setGeneratedImage] = useState(null);
    const [isLoading, setIsLoading] = useState(false);

    const handleInputChange = (e) => {
        setInputText(e.target.value);
    };

    const handleGenerateImage = async () => {
        setIsLoading(true);
        const response = await apiServices.generateImage({"prompt": inputText});
        setIsLoading(false);
        console.log("This is the response i have ::---", response);
        if (response) {
            setGeneratedImage(response?.data);
        }
    };

    console.log(generatedImage);

    const handleDownloadImage = () => {
        downloadImage(generatedImage);
    };

    return (
        <section className='w-full h-full p-14  flex justify-center items-center'>

            <div className="container mx-auto   p-16">
                <div className='flex justify-center h-80 shadow-lg' style={{ overflowY: 'auto' }}>
                    {isLoading ? (
                        <div className="spinner" /> 
                    ) : generatedImage ? (
                        <>
                            <img src={generatedImage} alt="Generated Image" className="max-w-full mb-4" />
                        </>
                    ) : (
                        <img src="https://images.nightcafe.studio/jobs/ogBIc50pY1WVacF3L8zM/ogBIc50pY1WVacF3L8zM.jpg?tr=w-1600,c-at_max" alt="Dummy Image" className="max-w-full mb-4" />
                    )}
                </div>
                <input
                    type="text"
                    value={inputText}
                    onChange={handleInputChange}
                    placeholder="Enter text..."
                    className="border border-gray-400 p-2 mb-4 w-full"
                />
                <button onClick={handleGenerateImage} className="bg-red-500 text-white px-4 py-2 rounded mr-4">Generate Image</button>
                <button onClick={handleGenerateImage} className="bg-yellow-500 text-white px-4 py-2 rounded mr-4">Download Image</button>
            </div>
        </section>
    );
};

export default ImageGenerator;
