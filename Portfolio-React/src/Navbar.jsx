import { Link, useLocation } from "react-router-dom";

function Navbar(){
    const location = useLocation();
    console.log("Current Location:",location);

    const showBack = location.pathname.startsWith("/projects/");
    console.log("Show Back?", showBack);

    return(
        <nav className="bg-blue-600 md:bg-slate-900 p-4 md:p-8 flex justify-center items-center gap-4 md:gap-12 transition-all duration-500">            
            <Link to="/" className={ location.pathname === "/" ? "active" : "" }> Home </Link>
            <Link to="/projects" className={ location.pathname === "/projects" ? "active" : "" }> Projects </Link>
            <Link to="/profileCard" className={ location.pathname === "/profileCard" ? "active" : "" }> Profile Card </Link>
            <Link to="/contact" className={ location.pathname === "/contact" ? "active" : "" }> Contact</Link>
            {showBack && <Link to="./projects"> Back </Link>}
        </nav>
    );
}

export default Navbar;