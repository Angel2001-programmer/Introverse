import styles from "./Charities.module.css";
import { charities } from '../../constants';
import TeamMemeber from "../TeamMember/teamMember";
import { Fragment } from "react";

const Charities = () => {
    return(
        <div>
						<h2>Helplines</h2>
						<p className={styles.paragraph}>
							If you are struggling with loneliness or anything please contact
							the following charities dont ever feel like you cant reach out
							because there are people who will help you.
						</p>

						{charities.map((charity) => (
                            <Fragment>
                                <TeamMemeber 
								width="680px"
                                profilepictrue={charity.image}  
                                hobby="" 
								description="" 
								height="450px"
								/>
								<h3>{charity.name}</h3>
								<p className={styles.paragraph}>{charity.desc}</p>
								<p className={styles.paragraph}>
									website: <a href={charity.website}>{charity.website}</a>
								</p>
                            </Fragment>
						))}
					</div>
    )
}

export default Charities;