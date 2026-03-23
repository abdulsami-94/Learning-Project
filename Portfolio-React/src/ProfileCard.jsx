function ProfileCard() {
    return(
        <div className="min-h-screen flex justify-center items-center bg-slate-900 p-10">
            <div className="bg-white rounded-xl shadow-2xl p-6 flex flex-col md:flex-row items-center gap-6 max-w-2xl w-full">
                <img src="https://imgs.search.brave.com/vp0EYQD3FX9O1T_vOFGhOUx62chHLqV1yPdyGvk_GWs/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvNTg3/ODA1MTU2L3ZlY3Rv/ci9wcm9maWxlLXBp/Y3R1cmUtdmVjdG9y/LWlsbHVzdHJhdGlv/bi5qcGc_cz02MTJ4/NjEyJnc9MCZrPTIw/JmM9Z2t2TERDZ3NI/SC04SGVRZTdKc2po/bE9ZNnZSQkprX3NL/VzlseWFMZ21Mbz0" alt="profilePic" className="w-32 h-32 rounded-full object-cover shadow-lg" />
                <div className="text-center md:text-left">
                    <h2 className="text-2xl font-bold text-slate-800">Abdul Sami</h2>
                    <p className="text-slate-500 mt-2">Full Stack Developer</p>
                    <button className="mt-4 px-6 py-2 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 hover:scale-105 transition-all">Follow Me</button>
                </div>
            </div>
           
        </div>
    );
}

export default ProfileCard;