import styles from "./signup.module.css";
import Button from "../Button/button"
import UserInput from "../UserInput/userInput"
import Card from "../Card/card";
import { useState, useContext } from "react";
import { SignUpContext, UserContext, NewUserContext } from "../../components/FinalProject/FinalProject";
import httpClient from "../../httpClient";
import { login } from "../../auth";
import { useDispatch } from "react-redux";
import { setSignIn } from "../../redux/slices/userSlice"

const SignUp = () => {
  const initialValues = {
    userName: "",
    firstName: "",
    lastName: "",
    email: "",
    password: "",
    confirmPSW: ""
  };

  // Are there any contexts or states that we don't need anymore?
  let SignedUp = null;
  const [isSignUp, setIsSignUp] = useContext(SignUpContext);
  const [isSignModal, setIsSignModal] = useContext(SignUpContext);
  const [isOpened, setIsOpened] = useContext(UserContext);
  const [newUser, setNewUser] = useContext(NewUserContext);
  const [count, setCount] = useState(5);
  const [newUserData, setNewUserData] = useState(initialValues);
  const [errorMessage, setErrorMessage] = useState("");

  const dispatch = useDispatch()

  // Function to register a new user, post the data to backend if legit, and log user in afterwards
  const registerUser = async () => {
    httpClient({
      method: "POST",
      url: "http://127.0.0.1:5000/user/register",
      data: {
        username: newUserData.userName,
        first_name: newUserData.firstName,
        last_name: newUserData.lastName,
        email: newUserData.email,
        password: newUserData.password
      }
    })
    .then((response) => {
      console.log(response)
      console.log(response.data.access_token)
      console.log(response.data.user)
      login(response.data.access_token)
      let name = response.data.user
      dispatch(setSignIn({name}))
      console.log(newUserData.userName, " has signed up")
      setNewUser(true)
    }).catch((error) => {
      if (error.response) {
        console.log(error.response)
        console.log(error.response.status)
        console.log(error.response.headers)
        if (error.response.status === 401) {
          alert("Invalid credentials");
        }
      }
    })
  };

  const handleValues = (e) => {
      setNewUserData({ ...newUserData, [e.target.name]: e.target.value});
  };

  // Need to refactor this! Make the error handling more efficient
  const handleForm = (e) => {
    e.preventDefault();
    
    if (newUserData.userName === "" || newUserData.userName.length === 0 &&
      newUserData.firstName === "" || newUserData.firstName.length === 0 &&
      newUserData.lastName === "" || newUserData.lastName.length === 0 &&
      newUserData.email === "" || newUserData.email.length === 0 &&
      newUserData.password === "" || newUserData.password.length === 0 &&
      newUserData.confirmPSW === "" || newUserData.confirmPSW.length === 0){
      setNewUser(false);
      return setErrorMessage("Inputs cannot be empty.");
    } else if (newUserData.password !== newUserData.confirmPSW){
      setErrorMessage("Password does not match.");
      setNewUser(false);
    } else if (newUserData.userName.length >= 30){
      setErrorMessage("Username must not be more than 30 characters.");
      setNewUser(false);
    } else if (newUserData.firstName.length >= 50){
      setErrorMessage("First name must be no more than 50 characters.");
      setNewUser(false);
    } else if (newUserData.lastName.length >= 50){
      setErrorMessage("Last name must be no more than 50 characters.");
      setNewUser(false);
    } else if (newUserData.email.length >= 254){
        setErrorMessage("Email address is too long.");
      setNewUser(false);
    } else if (newUserData.password.length >= 72 || newUserData.password.length < 8){
      setErrorMessage("Password length is invalid.");
      setNewUser(false);
    } else {
      setErrorMessage("");
      registerUser();
    }
  }

  // We can delete this right? The constant counting
  // console.log(newUserData.userName.length);

  if (newUser === true){
    setTimeout(() => {
    if(count > 0){
      setCount(count - 1)
    } else {
      setIsSignModal(false);
      setIsOpened(false);
      console.log('Login successful')
    }
    }, 1000);

    return (
    <Card>
      <div className={styles.container}>
      <h2 className={styles.accountCreation}>Account creation successful! Welcome to our community</h2>
      <h2 className={styles.bottomText}>This will disappear in {count}</h2>
      </div>
    </Card>
    )
  }


  return (
      <Card>
      <form onSubmit={handleForm}>
      <UserInput 
      isCloseIcon="←"
      isClose={() => setIsSignModal(false)
      }
      className="userInput"
      title="Sign up" 
      for="userName" 
      type="text" 
      name="userName"
      value={newUserData.userName} 
      onValue={handleValues}
      placeholder="Username"
      labelName="Username"
      />

      <div className={styles.nameContainer}>
      <UserInput
      className={styles.UIName}
      title=""  
      for="firstName" 
      type="text" 
      name="firstName"
      value={newUserData.firstName} 
      onValue={handleValues}
      placeholder="First Name"
      labelName="First Name"
      />

      <UserInput 
      title="" 
      for="lastName" 
      type="text" 
      name="lastName"
      value={newUserData.lastName} 
      onValue={handleValues}
      placeholder="Last name"
      labelName="Last name"
      />
      </div>

      <UserInput 
      title="" 
      for="email" 
      type="email" 
      name="email"
      value={newUserData.email} 
      onValue={handleValues}
      placeholder="Email"
      labelName="Email"
      />

      <UserInput 
      title="" 
      for="password" 
      type="password" 
      name="password"
      value={newUserData.password} 
      onValue={handleValues}
      placeholder="Password"
      labelName="Password"
      />

      <UserInput 
      title="" 
      for="confirmPSW" 
      type="password" 
      name="confirmPSW"
      value={newUserData.confirmPSW} 
      onValue={handleValues}
      placeholder="Confirm Password"
      labelName="Confirm Password"
      />
      
      <div className={styles.bottomContainer}>
      <p className="errorMessage">{errorMessage}</p>
      <p>Password must be at least 8 characters</p>
      <Button 
      type="submit" 
      text="Create an account"
      label="submitBtn"
      UIcolor="linear-gradient(#D000AF, #9000A8)"
      borderColor="purple"
      dropShadow="#AD0B9A70 5px 5px 5px"
      />
      </div>
      </form>
      </Card>
  );
}

export default SignUp;