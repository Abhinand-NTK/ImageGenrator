import axios from "axios";

const baseURL = 'http://127.0.0.1:8000'; 

const userAPI = axios.create({
  baseURL,
});

const signup = async (userData) => {
  try {
    const response = await userAPI.post('/signup', userData);
    return response; 
  } catch (error) {
    console.log(error.response.status)
    console.error('Error signing up:', error);
    throw error; 
  }
};

const login = async (userData) => {
  console.log("This is the user data :--",userData)
  try {
    const response = await userAPI.post('/login', userData);
    return response; 
  } catch (error) {
    console.error('Error logging in:', error);
    throw error; 
  }
};

const generateImage = async (promptData) => {
  console.log(promptData)
  try {
    const response = await userAPI.post('/generate_image', promptData);
    return response.data;
  } catch (error) {
    console.error('Error generating image:', error);
    throw error;
  }
};



const getUserInfo = async () => {
  try {
    const response = await userAPI.get('/user');
    return response; 
  } catch (error) {
    console.error('Error getting user info:', error);
    throw error; 
  }
};

const getToken = async (userData) => {
  console.log("This is the userdata :--",userData)
  try {
    const response = await userAPI.post('/token', userData);
    return response; 
  } catch (error) {
    console.error('Error obtaining token:', error);
    throw error; 
  }
};

export const apiServices = {
  signup,
  login,
  getUserInfo,
  getToken,
  generateImage,
};
