import React, { useState } from "react";
import axios from "axios";

const Transits = () => {
    const [transits, setTransits] = useState({});
    const [date, setDate] = useState("");

    const fetchTransits = async () => {
        const response = await axios.post("http://127.0.0.1:5000/transits", { date });
        setTransits(response.data);
    };

    return (
        <div>
            <h2>Planetary Transits</h2>
            <input type="date" onChange={(e) => setDate(e.target.value)} />
            <button onClick={fetchTransits}>Get Transits</button>
            <pre>{JSON.stringify(transits, null, 2)}</pre>
        </div>
    );
};

export default Transits;
