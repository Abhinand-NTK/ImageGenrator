
import React from 'react';
import { Formik, Form, Field } from 'formik';
import { Link, useNavigate } from 'react-router-dom';
import { apiServices } from '../api/UsersApi';


const Login = () => {
    const navigate = useNavigate();

    const initialValues = {
        username: '',
        password: ''
    };

    const onSubmit = async (values, actions) => {
        console.log(values)
        const response = await apiServices.getToken(values)

        console.log("The data that is coming from the back end as the jwt::--",response)
        if (response.status == 200) {
            navigate('/imagegenerator');
        }
        console.log('Form submitted with values:', values);
        actions.setSubmitting(false);
    };

    return (
        <section className='w-full h-full p-4 sm:p-12 flex justify-center items-center'>
            <Formik
                initialValues={initialValues}
                onSubmit={onSubmit}
            >
                {({ isSubmitting }) => (
                    <Form className=" mt-32 form_main flex flex-col items-center justify-center bg-white sm:w-96 p-8 rounded-lg shadow-md relative overflow-hidden"> {/* Modified for responsiveness */}
                        <p className="heading text-2xl font-bold text-gray-700 mb-4">Login</p>
                        <div className="inputContainer w-full relative">
                            <Field
                                type="username"
                                className="inputField m-2 sm:m-5 w-full pl-8 border-b-2 border-gray-300 focus:border-purple-500 outline-none"
                                id="username"
                                name="username"
                                placeholder="Username"
                            />
                        </div>

                        <div className="inputContainer w-full relative">
                            <Field
                                type="password"
                                className="inputField m-2 sm:m-5 w-full pl-8 border-b-2 border-gray-300 focus:border-purple-500 outline-none"
                                id="password"
                                name="password"
                                placeholder="Password"
                            />
                        </div>
                        <button
                            type="submit"
                            id="button"
                            disabled={isSubmitting}
                            className="w-full m-2 sm:m-5 bg-purple-600 text-white font-semibold py-2 px-4 rounded hover:bg-purple-700 transition duration-300"
                        >
                            {isSubmitting ? 'Submitting...' : 'Submit'}
                        </button>
                        <Link to="/signup" className="forgotLink text-sm font-semibold text-purple-700 mt-2">
                            Register
                        </Link>
                    </Form>
                )}
            </Formik>
        </section>
    );
};

export default Login;
