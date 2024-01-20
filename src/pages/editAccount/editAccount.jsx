import { Fragment, useState, React, useEffect, useContext } from 'react';
import styles from './editAccount.module.css';
import NavBar from '../../components/NavBar/navbar';
import DropDownMenu from '../../components/DropDownMenu/dropDownMenu';
import MobileNav from '../../components/MobileNav/MobileNav';
import EditPosts from "../../components/EditPosts/EditPosts";
import EditBanner from "../../components/EditBanner/EditBanner";
import EditDetailsProfile from "../../components/EditProfileDetails/EditProfileDetails";
import { UserNameContext } from "../../components/FinalProject/FinalProject";

import axios from 'axios';
const EditAccount = () => {
	const [isPressed, setIsPressed] = useState(false);
	const [posts, setPosts] = useState(null);
	const [filteredposts, setfilteredposts] = useState(null);
	const [UserName, setUserName] = useContext(UserNameContext);

	console.log(UserName)

	let error = null;
	let user = "BlaxeXD"
	let filteredList = null;

	useEffect(() => {
		const getForms = async () => {
			const res = await axios.get("http://localhost:5000/forum")
			.then(res => { 
			  setPosts(res.data)    
			  filteredList = res.data.filter((list) => list.post_author === "User2")
    		  console.log(filteredList);
			  setfilteredposts(filteredList);
			  if(filteredList.length === 0){
				error = <h2>No Posts Yet.</h2>
				setPosts(null)
			  }
			})
			.catch(err => {
			  setPosts(null);
			  // APIres = null;
			  console.log(err);
			  error = <h2>No Posts Yet.</h2>});
		}
		getForms();
		// getAPI();
	  }, [])


	return (
		<Fragment>
			<NavBar isPressed={isPressed} onChangePressed={setIsPressed} />
			<MobileNav/>
			<DropDownMenu isPressed={isPressed} setIsPressed={setIsPressed} />
			<main className={styles.main}>
				<EditBanner/>
				{posts !== null?
				<EditPosts data={filteredposts}/>
				:
				<div className={styles.NoPosts}>
				<h2>No Posts Yet.</h2>				
				</div>
				}
				{/* <EditDetailsProfile/> */}
			</main>
		</Fragment>
	);
};

export default EditAccount;
