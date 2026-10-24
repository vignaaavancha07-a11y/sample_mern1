import Header_component from "./Components/Header_component";
import Footer_component from "./Components/Footer_component";
import Home from './pages/Home'
import About from './pages/About'
import Contact from './pages/Contact'
import Login from './pages/Login'
import {Routes,Route} from 'react-router-dom'
function App(){
  return(
    <div>
      <Header_component></Header_component>
      <Routes>
        <Route path="/" element={<Home/>}></Route>
        <Route path="/login" element={<Login/>}></Route>
        <Route path="/about" element={<About/>}></Route>
        <Route path="/contact" element={<Contact/>}></Route>

      </Routes>
      <Footer_component></Footer_component>
    </div>
  )
}
export default App