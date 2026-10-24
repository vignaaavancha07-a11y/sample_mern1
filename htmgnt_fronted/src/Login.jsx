import { useState } from "react"
function Login(){
    let [emailid,setEmailid]=useState("")
    let [password,setPassword]=useState("")

    return(
        <div>
            <form>
                <input type="text" placeholder="Enter emailed"></input><br/>
                <input type="password" placeholder="Enter password"></input><br/>
                <button type="submit">Login</button>
            </form>

        </div>
    )
}
export default Login