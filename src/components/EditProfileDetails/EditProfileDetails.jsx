import styles from "./EditProfileDetails.module.css";
import editProfile from '../../assets/images/editProfile.svg';

const EditPosts = () => {
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
