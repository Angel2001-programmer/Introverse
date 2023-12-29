import styles from "./ForumItem.module.css";

const ForumItem = props => {
    let profile = null;
    let comments = null;
    if (props.icon !== ""){
        profile = <img className={styles.icon} src={props.icon} alt="Icon"/>
    } else {
        profile = <img className={styles.icon} src={require("../../assets/images/logos/user.png")} alt="Icon"/>
    }

    if (!props.isComments){
        comments = null;
    } else {
        comments = 
        <div className={styles.commentContainer}>
            <img className={styles.comment} src={require("../../assets/icons/comments.png")} alt="comments"/>
            <p>0</p>
        </div>  
    }

    return(
        <div className={styles.row} onClick={props.click}>
            {profile}
            <div className={styles.Textcolumn}>
            <p className={styles.title}>{props.title}</p>
            <p className={styles.subtitle}>{props.userName}</p>
            {comments}            
            </div>
        </div>
    )
}

export default ForumItem;