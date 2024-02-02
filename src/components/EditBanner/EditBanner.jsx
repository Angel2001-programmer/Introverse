import styles from "./EditBanner.module.css";
import profile from '../../assets/images/logos/user.png';
import { Fragment, useContext } from "react";
import { UserNameContext } from "../../components/FinalProject/FinalProject";
import { useSelector } from "react-redux"
import { selectCurrentUser } from "../../redux/slices/userSlice"


const EditBanner = () => {
    const [UserName, setUserName] = useContext(UserNameContext);
    const user = useSelector(selectCurrentUser)
    // const greeting = useSelector(state => state.user)

    console.log(user)

    const welcome = user ? `${user.name}` : "Guest"

    return (
        <Fragment>
        <div className={styles.banner}></div>
				<div className={styles.profile}>
					<img className={styles.profilePicture} src={profile} alt='profile.' />
					<h4 className={styles.profileName}>{welcome}</h4>
		</div>
        </Fragment>
    )
}

export default EditBanner;
