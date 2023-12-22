import { Fragment } from "react";
import styles from './teamMember.module.css';
import user from "../../assets/img/user.png";

const TeamMemeber = props => {
    return(
        <Fragment>
        <section className={styles.profile}>
          {props.profilepictrue !== "" ? 
          <img className={styles.profileIMG} 
          src={props.profilepictrue} 
          alt={props.name}
          style={{height: props.height, width: props.width}}/>
          : 
          <div className={styles.profileContainer}>
            <img className={styles.profileIMG} 
            src={user} 
            alt="empty profile."/>
          </div> }
          <h2>{props.name}</h2>
          {props.description === "" && props.hobby === "" ?
          <div></div>
          : <div> 
            <h4 className={styles.favouriteActivity}>Favourite hobby</h4>
            <li>{props.hobby}</li>
            <h4 className={styles.favouriteActivity}>Description</h4>
            <li>{props.description}</li>
            </div>
          }
      </section>
        </Fragment>
    )
}
export default TeamMemeber;