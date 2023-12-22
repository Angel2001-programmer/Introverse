import { Link } from 'react-router-dom';
import { NewUserContext } from "../../components/FinalProject/FinalProject"
import { useContext } from 'react';
import { useAuth, logout } from "../../auth";
import httpClient from "../../httpClient";


// set log out functionality here?
const DropDownMenu = props => {
  const [newUser, setNewUser] = useContext(NewUserContext);

  // Function to log out the user
  function logMeOut() {
    httpClient({
      method: "POST",
      url: "http://localhost:5000/logout"
    })
    .then((response) => {
      logout()
      alert("You have successfully logged out")
    }).catch((error) => {
      if (error.response) {
        console.log(error.response)
        console.log(error.response.status)
        console.log(error.response.error)
      }
    })

  }

    return(
        props.isPressed?
            <div className="dropDownMenuContainer">
              <div className="dropDownMenu">
              <Link className='link' to="/profile">
                <div className='dropMenuItem'>
                <p>Profile</p>
                </div></Link>
                <div className='dropMenuItem' onClick={() => {
                  setNewUser(false);
                  props.setIsPressed(false);
                  }}>
                <Link className='link' to="/finalProject" onClick={logMeOut}><p>Sign Out</p></Link>
                </div>
              </div>
            </div>
            : null
    )
}

export default DropDownMenu;