import styles from "./EditProfileDetails.module.css";
import editProfile from '../../assets/images/editProfile.svg';
import React, { useEffect, useState } from "react"
import httpClient from "../../httpClient";
import { useSelector } from "react-redux"
import { selectCurrentUser } from "../../redux/slices/userSlice"

// Have added an API call ish but no idea how to get it into the profile box or how to convert the profile box to view rather than edit, tried to copy recommendations.js
// Think would be cool to have the component as view only initially with an "edit" button, that then allows you to make a put or post request to edit certain fields

const EditPosts = () => {

  const user = useSelector(selectCurrentUser)
  const [List, setList] = useState([]);
  const token = localStorage.getItem('REACT_TOKEN_AUTH_KEY')
  console.log(token)

// 	useEffect(() => {
//     fetch("http://localhost:5000/user/current_user/", {headers: {"Authorization": `Bearer ${JSON.parse(token)}`}})
//     .then(res => res.json())
//     .then(data => {
//       console.log(data)
//     })
//     .catch(error => console.log(error))
//     }, [token]
//     );


// const fetchSecretData = () => {
//   const URL = "http://localhost:5000/user/current_user/"
//   const headers = {"Authorization": `Bearer ${JSON.parse(token)}`};
//   fetch(URL, {headers})
//   .then(response => response.json())
//   .then(data => console.log(data));
// }
// fetchSecretData()

//   useEffect(() => {
//     const getAPI = async () => {
//       try {
//         const response = await httpClient.get("http://localhost:5000/user/current_user/", {headers: {"Authorization": `Bearer ${JSON.parse(token)}`}});
//         console.log(response.data)
//       } catch(error) {
//       console.log(error)
//     }
//     };
//     getAPI()
//   }, [user.name, token]);


// 	useEffect(() => {
//     const getAPI = async () => {
//       try {
//         const response = await httpClient.get("http://localhost:5000/user/members/" + user.name);
//         console.log(response.data)
//       } catch(error) {
//       console.log(error)
//     }
//     };
//     getAPI()
//   }, [user.name]);

  console.log()

    return (
		<form className={styles.EditAccountform}>
			<div className={styles.row}>
				<label>FirstName:</label>
				<input
					className={styles.editInput}
					type='text'
					name='text'
					placeholder='Angel'
					readOnly='readonly'
				/>
				<img
					className={styles.imageButton}
					src={editProfile}
					alt='edit Password.'
				></img>
			</div>
			<div className={styles.row}>
				<label>LastName:</label>
				<input
					className={styles.editInput}
					type='text'
					name='text'
					placeholder='sdgsgjkshjfkshjfkash'
					readOnly='readonly'
				/>
				<img
					className={styles.imageButton}
					src={editProfile}
					alt='edit Password.'
				></img>
			</div>
			<div className={styles.row}>
				<label>UserName:</label>
				<input
					className={styles.editInput}
					type='text'
					name='text'
					placeholder='BlaxeXD'
					readOnly='readonly'
				/>
				<img
					className={styles.imageButton}
					src={editProfile}
					alt='edit Password.'
				></img>
			</div>
			<div className={styles.row}>
				<label>Email:</label>
				<input
					className={styles.editInput}
					type='email'
					name='text'
					placeholder='angelhhhhh3000@yahoo.com'
					readOnly='readonly'
				/>
				<img
					className={styles.imageButton}
					src={editProfile}
					alt='edit Password.'
				></img>
			</div>
			<div className={styles.row}>
				<label>Password:</label>
				<input
					className={styles.editInput}
					type='password'
					name='password'
					placeholder='currentPassword'
					readOnly='readonly'
				/>
				<img
					className={styles.imageButton}
					src={editProfile}
					alt='edit Password.'
				></img>
			</div>
		</form>
    )
}

export default EditPosts;
