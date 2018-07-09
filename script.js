import {sleep} from "k6";
import http from "k6/http";

export default function() {
	http.get("http://test.loadimpact.com");
	sleep(Math.random() * 20);
};
