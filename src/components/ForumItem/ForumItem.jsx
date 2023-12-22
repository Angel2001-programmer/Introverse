import styles from "./ForumItem.module.css";

const ForumItem = props => {
    let profile = null;
    if (props.icon !== ""){
        profile = <img className={styles.icon} src={props.icon} alt="Icon"/>
    } else {
        profile = <img className={styles.icon} src={require("../../assets/images/logos/user.png")} alt="Icon"/>
    }

    return(
        <div className={styles.row} onClick={props.click}>
            {profile}
            <div className={styles.Textcolumn}>
            <p className={styles.title}>{props.title}</p>
            <p className={styles.subtitle}>{props.userName}</p>
            </div>
        </div>
    )
}

export default ForumItem;