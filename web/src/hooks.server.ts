import { connectToDatabase } from "$lib/server/services/database.service";

connectToDatabase().then(() => {
	console.log('Mongo started');
}).catch(e => {console.error(e)})