import { start_mongo } from "$lib/mongo";

start_mongo().then(() => {
	console.log('Mongo started');
}).catch(e => {console.error(e)})