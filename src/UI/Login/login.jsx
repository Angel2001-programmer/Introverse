import styles from "./login.module.css";
import Button from "../Button/button"
import UserInput from "../UserInput/userInput"
import Card from "../Card/card";
import { useContext, useState } from 'react'
import { UserContext, SignUpContext, NewUserContext, UserNameContext } from "../../components/FinalProject/FinalProject";
import httpClient from "../../httpClient";
import { login } from "../../auth";
import { useDispatch } from "react-redux";
import { setSignIn } from "../../redux/slices/userSlice"


function Login() {
  const [isOpened, setIsOpened]  = useContext(UserContext);
  const [isSignModal, setIsSignModal] = useContext(SignUpContext);
  const [newUser, setNewUser] = useContext(NewUserContext);
  const [userName, setUserName] = useContext(UserNameContext);

  const initialValues = {
    userName: "",
    password: ""
  };
  // This is just a test to see if login works with data.
  const [userData, setUserData] = useState(initialValues);
  const [errorMessage, setErrorMessage] = useState(null);
  let createAccount = null;

  const dispatch = useDispatch()

  // Function to fetch user data from database, log in user if successful
  const loginUser = async () => {
    httpClient({
      method: "POST",
      url: "http://localhost:5000/user/login",
      data: {
        username: userData.userName,
        password: userData.password
      }
    })
    .then((response) => {
      console.log(response)
      console.log(response.data.access_token)
      console.log(response.data.user)
      login(response.data.access_token)
      let name = response.data.user
      dispatch(setSignIn({name}))
      console.log(userData.userName, " has logged in")
      setIsOpened(false)
      setNewUser(true)
      setIsSignModal(false)
      alert("Welcome you have successfully logged in.")
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

  //Set new keystroke to UserData values.
  const handleValues = (e) => {
      setUserData({ ...userData, [e.target.name]: e.target.value});
  };

  const handleLogin = (e) => {
    //Prevents form from refreshing when Sign button is clicked.
    e.preventDefault();
    if(userData.userName.trim().length === 0 || userData.password.trim().length === 0){
        setErrorMessage(<p className={styles.errorMessage}>Inputs cannot be empty</p>)
    } else {
        setErrorMessage("")
        loginUser()
    }
  }

  //Check if Modal is opened.
  if(isOpened){
    createAccount = <div className={styles.login}>
        <form onSubmit={handleLogin}>
        <UserInput 
        isCloseIcon="X"
        isClose={() => setIsOpened(false)}
        title="Login" 
        for="userName" 
        type="text" 
        name="userName"
        value={userData.userName}
        onValue={handleValues}
        placeholder="UserName"
        labelName="UserName"
        />

        <UserInput 
        title="" 
        for="password" 
        type="password" 
        name="password"
        value={userData.password} 
        onValue={handleValues}
        placeholder="Password"
        labelName="Password"
        />
        {errorMessage}
        <div className={styles.bottomContainer}>

        <Button 
        type="submit" 
        text="Sign in" 
        UIcolor="linear-gradient(#D000AF, #9000A8)"
        borderColor="purple"
        dropShadow="#AD0B9A70 5px 5px 5px"
        paddingToRight="70px"
        paddingToLeft="70px"
        />
        <div className={styles.noAccount}>
        <h2 className={styles.signUp}>Don't have an account? </h2>
        <h2 className={styles.signUpLink} 
        onClick={() => {
            setIsSignModal(true)
        }
        }
        >Sign up</h2>
        </div>
        </div>
        </form>
    </div>
  }
  return(
      <Card className={styles.modal}>
          {createAccount}
      </Card>        
  )
}

export default Login;