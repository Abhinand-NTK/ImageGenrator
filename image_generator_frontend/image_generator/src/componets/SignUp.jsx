import React from 'react';
import { Formik, Form, Field } from 'formik';
import { Link, useNavigate } from 'react-router-dom';
import { apiServices } from '../api/UsersApi';
import toast from 'react-hot-toast';

const SignUp = () => {
    const navigate = useNavigate();

    const handleSubmit = async (values, actions) => {
        console.log(values);
        try {
            const response = await apiServices.signup(values);
            console.log("This is the response", response.status);
            if (response?.status === 200) {
                toast.success('User is created', {
                    duration: 5000,
                    style: {
                        marginTop: '100px',
                    },
                });
                console.log("success");
                // Navigate to the login page
                navigate('/');
            }
            console.log('API Response:', response);
        } catch (error) {
            console.error('API Error:', error);
        }
        // Reset form values
        actions.resetForm();
        actions.setSubmitting(false);
    };

    return (
        <Formik
            initialValues={{ email: '', password: '', user_type: '' }}
            onSubmit={handleSubmit}
        >
            {({ isSubmitting }) => (
                <section className='w-full h-full p-14  flex justify-center items-center'>
                    <Form className="form_main flex flex-col items-center justify-center bg-white p-6 sm:p-16 md:p-24 mt-12 rounded-lg shadow-md relative overflow-hidden">
                        <p className="heading text-2xl font-bold text-gray-700 mb-4">Sign Up</p>
                        <div className="inputContainer w-full relative">
                            <Field
                                type="email"
                                className="inputField w-full pl-8 pr-3 py-2 border-b-2 border-gray-300 focus:border-purple-500 outline-none"
                                id="email"
                                name="email"
                                placeholder="Email"
                            />
                        </div>

                        <div className="inputContainer w-full relative">
                            <Field
                                type="password"
                                className="inputField w-full pl-8 pr-3 py-2 border-b-2 border-gray-300 focus:border-purple-500 outline-none"
                                id="password"
                                name="password"
                                placeholder="Password"
                            />
                        </div>

                        <div className="inputContainer w-full relative">
                            <Field
                                type="text"
                                className="inputField w-full pl-8 pr-3 py-2 border-b-2 border-gray-300 focus:border-purple-500 outline-none"
                                id="user_type"
                                name="user_type"
                                placeholder="User Type"
                            />
                        </div>

                        <button
                            type="submit"
                            id="button"
                            disabled={isSubmitting}
                            className="w-full mt-5 bg-purple-600 text-white font-semibold py-2 px-4 rounded hover:bg-purple-700 transition duration-300"
                        >
                            {isSubmitting ? 'Submitting...' : 'Sign Up'}
                        </button>
                        <Link to="/" className="forgotLink text-sm font-semibold text-purple-700 mt-2">
                            Login
                        </Link>
                    </Form>
                </section>
            )}
        </Formik>
    );
};

export default SignUp;
