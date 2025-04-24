import React, { useState } from "react";
import {
  MDBBtn,
  MDBContainer,
  MDBCard,
  MDBCardBody,
  MDBRow,
  MDBCol,
  MDBInput,
  MDBProgress,
  MDBProgressBar
} from "mdb-react-ui-kit";
import { 
  Mail, 
  User,
  Lock,
  UserCircle,
  Users,
  Calendar,
  Ruler,
  Weight,
  Target,
  Activity,
  ChevronRight,
  ChevronLeft,
  Camera,
  AtSign,
  Shield,
  Heart,
  Scale,
  Dumbbell
} from 'lucide-react';
import axiosInstance from "../../axiosInstance";

const Register = () => {
  const [formData, setFormData] = useState({
    email: "",
    username: "",
    password: "",
    firstName: "",
    lastName: "",
    age: "",
    sexe: "",
    weight: "",
    height: "",
    goalWeight: "",
    activityLevel: "",
    profilePicture: ""
  });

  const [currentStep, setCurrentStep] = useState(1);
  const [error, setError] = useState("");

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleRegister = async () => {
    try {
      const response = await axiosInstance('register-client/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: formData.email,
          username: formData.username,
          password: formData.password, // Ensure password handling on the backend
          first_name: formData.firstName,
          last_name: formData.lastName,
          age: formData.age,
          sexe: formData.sexe,
          weight: formData.weight,
          height: formData.height,
          goal_weight: formData.goalWeight,
          activity_level: formData.activityLevel,
          profile_picture: formData.profilePicture,
        }),
      });
  
      const result = await response.json();
  
      if (response.ok) {
        console.log('Registration successful:', result);
        // You can add any redirection or confirmation here
      } else {
        throw new Error(result.detail || 'Registration failed');
      }
    } catch (err) {
      setError(err.message || 'Registration failed. Please try again.');
    }
  };

  const handleNextStep = () => {
    if (currentStep < 3) setCurrentStep(currentStep + 1);
  };

  const handlePrevStep = () => {
    if (currentStep > 1) setCurrentStep(currentStep - 1);
  };

  const stepTitles = {
    1: "Welcome to Online Workout",
    2: "Personal Information",
    3: "Fitness Profile"
  };

  const CustomInput = ({ icon: Icon, label, name, type, value, onChange, className = "" }) => (
    <div className="custom-input-container position-relative mb-4">
      <div className="position-absolute" style={{ left: '15px', top: '50%', transform: 'translateY(-50%)', zIndex: 1 }}>
        <Icon size={18} strokeWidth={2} className="text-muted" />
      </div>
      <MDBInput
        label={label}
        name={name}
        type={type}
        value={value}
        onChange={onChange}
        className={`${className}`}
        style={{ 
          height: '45px', 
          fontSize: '0.9rem',
          paddingLeft: '45px'
        }}
        labelStyle={{
          marginLeft: '30px' // Déplace le label pour éviter la superposition avec l'icône
        }}
      />
    </div>
  );

  const CustomSelect = ({ icon: Icon, name, value, onChange, options }) => (
    <div className="custom-select-container position-relative mb-4">
      <div className="position-absolute" style={{ left: '15px', top: '50%', transform: 'translateY(-50%)', zIndex: 1 }}>
        <Icon size={18} strokeWidth={2} className="text-muted" />
      </div>
      <select
        className="form-select"
        name={name}
        value={value}
        onChange={onChange}
        style={{ 
          height: '45px', 
          fontSize: '0.9rem',
          paddingLeft: '45px'
        }}
      >
        {options.map(option => (
          <option key={option.value} value={option.value}>{option.label}</option>
        ))}
      </select>
    </div>
  );

  return (
    <MDBContainer className="my-5">
      <MDBCard className='text-black m-5' style={{ borderRadius: '25px' }}>
        <MDBCardBody className="p-5">
          <MDBRow className="justify-content-center">
            <MDBCol md='10' lg='6' className='order-2 order-lg-1'>
              <div className="text-center mb-4">
                <h3 className="text-center h1 fw-bold mb-5 mx-1 mx-md-4 mt-4">
                  {stepTitles[currentStep]}
                </h3>
              </div>

              {error && (
                <div className="alert alert-danger" role="alert">
                  {error}
                </div>
              )}

              <div className="px-4">
                {currentStep === 1 && (
                  <>
                    <CustomInput
                      icon={Mail}
                      label="Email"
                      name="email"
                      type="email"
                      value={formData.email}
                      onChange={handleChange}
                    />
                    <CustomInput
                      icon={User}
                      label="Username"
                      name="username"
                      type="text"
                      value={formData.username}
                      onChange={handleChange}
                    />
                    <CustomInput
                      icon={Lock}
                      label="Password"
                      name="password"
                      type="password"
                      value={formData.password}
                      onChange={handleChange}
                    />
                  </>
                )}

                {currentStep === 2 && (
                  <>
                    <div className="row">
                      <div className="col-6">
                        <CustomInput
                          icon={UserCircle}
                          label="First Name"
                          name="firstName"
                          type="text"
                          value={formData.firstName}
                          onChange={handleChange}
                        />
                      </div>
                      <div className="col-6">
                        <CustomInput
                          icon={UserCircle}
                          label="Last Name"
                          name="lastName"
                          type="text"
                          value={formData.lastName}
                          onChange={handleChange}
                        />
                      </div>
                    </div>
                    <div className="row">
                      <div className="col-6">
                        <CustomInput
                          icon={Calendar}
                          label="Age"
                          name="age"
                          type="number"
                          value={formData.age}
                          onChange={handleChange}
                        />
                      </div>
                      <div className="col-6">
                        <CustomSelect
                          icon={Users}
                          name="sexe"
                          value={formData.sexe}
                          onChange={handleChange}
                          options={[
                            { value: "", label: "Select sexe" },
                            { value: "male", label: "Male" },
                            { value: "female", label: "Female" },
                            { value: "other", label: "Other" }
                          ]}
                        />
                      </div>
                    </div>
                  </>
                )}

                {currentStep === 3 && (
                  <>
                    <div className="row">
                      <div className="col-6">
                        <CustomInput
                          icon={Ruler}
                          label="Height (cm)"
                          name="height"
                          type="number"
                          value={formData.height}
                          onChange={handleChange}
                        />
                      </div>
                      <div className="col-6">
                        <CustomInput
                          icon={Weight}
                          label="Weight (kg)"
                          name="weight"
                          type="number"
                          value={formData.weight}
                          onChange={handleChange}
                        />
                      </div>
                    </div>

                    <CustomSelect
                      icon={Activity}
                      name="activityLevel"
                      value={formData.activityLevel}
                      onChange={handleChange}
                      options={[
                        { value: "", label: "Activity Level" },
                        { value: "sedentary", label: "Sedentary" },
                        { value: "light", label: "Lightly active" },
                        { value: "moderate", label: "Moderately active" },
                        { value: "active", label: "Active" },
                        { value: "very_active", label: "Very active" }
                      ]}
                    />

                    <CustomInput
                      icon={Target}
                      label="Goal Weight (kg)"
                      name="goalWeight"
                      type="number"
                      value={formData.goalWeight}
                      onChange={handleChange}
                    />

                    <CustomInput
                      icon={Camera}
                      label="Profile Picture URL"
                      name="profilePicture"
                      type="text"
                      value={formData.profilePicture}
                      onChange={handleChange}
                    />
                  </>
                )}

                <MDBProgress className="mb-4" height='20'>
                  <MDBProgressBar 
                    width={(currentStep / 3) * 100} 
                    valuemin={0} 
                    valuemax={100}
                  >
                    Step {currentStep} of 3
                  </MDBProgressBar>
                </MDBProgress>

                <div className="d-flex justify-content-between">
                  {currentStep > 1 && (
                    <MDBBtn 
                      color='light'
                      className='mb-4'
                      onClick={handlePrevStep}
                    >
                      <ChevronLeft size={20} className="me-2" />
                      Previous
                    </MDBBtn>
                  )}
                  
                  {currentStep < 3 ? (
                    <MDBBtn 
                      className='mb-4 ms-auto'
                      onClick={handleNextStep}
                    >
                      Next
                      <ChevronRight size={20} className="ms-2" />
                    </MDBBtn>
                  ) : (
                    <MDBBtn 
                      className='mb-4 ms-auto'
                      color='success'
                      onClick={handleRegister}
                    >
                      Complete Registration
                      <ChevronRight size={20} className="ms-2" />
                    </MDBBtn>
                  )}
                </div>
              </div>
            </MDBCol>

            <MDBCol md='10' lg='6' className='order-1 order-lg-2 d-flex align-items-center'>
              <div className="text-center w-100">
                <img
                  src="https://img.freepik.com/photos-gratuite/homme-athletique-pratiquant-gymnastique-pour-rester-forme_23-2150989957.jpg"
                  className="img-fluid"
                  alt="Registration"
                  style={{ maxHeight: '600px', objectFit: 'cover' }}
                />
              </div>
            </MDBCol>
          </MDBRow>
        </MDBCardBody>
      </MDBCard>
    </MDBContainer>
  );
};

export default Register;