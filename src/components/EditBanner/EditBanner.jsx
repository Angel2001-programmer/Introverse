import styles from "./EditBanner.module.css";
import profile from '../../assets/images/logos/user.png';
import { Fragment, useContext } from "react";
import { UserNameContext } from "../../components/FinalProject/FinalProject";


const EditBanner = () => {
    const [UserName, setUserName] = useContext(UserNameContext);

    return (
        <Fragment>
        <div className={styles.banner}></div>
				<div className={styles.profile}>
					<img className={styles.profilePicture} src={profile} alt='profile.' />
					<h4 className={styles.profileName}>User2</h4>
		</div>
        </Fragment>
    )
}

export default EditBanner;
