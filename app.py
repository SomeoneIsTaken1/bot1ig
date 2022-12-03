import nextcord
import os

client = nextcord.Client()

@client.event
async def on_ready():
	guild = client.get_guild(1045680764261507072)
	channel = guild.get_channel(1047209490392551445)
	message = await channel.fetch_message(1047223457877852170)
	'''await message.add_reaction("😆")
	await message.add_reaction("🏛️")
	await message.add_reaction("👑")
	await message.add_reaction("👸")
	await message.add_reaction("🤴")
	await message.add_reaction("💡")
	await message.add_reaction("💂")'''
	print(f'Logged as {client.user}')

@client.event
async def on_raw_reaction_add(reaction):
	guild = client.get_guild(1045680764261507072)
	channel = guild.get_channel(1047209490392551445)
	message = await channel.fetch_message(1047223457877852170)
	if reaction.member in [user if i.emoji != reaction.emoji.name else "" for i in message.reactions for user in await i.users().flatten()]:
		await message.remove_reaction(reaction.emoji, reaction.member)
		return
	if reaction.message_id == 1047223457877852170:
		if reaction.emoji.name == "👨‍💼":
			role = guild.get_role(1048612594426064936)
			await reaction.member.add_roles(role)
		if reaction.emoji.name == "😆":
			role = guild.get_role(1048612679641735228)
			await reaction.member.add_roles(role)
		if reaction.emoji.name == "🏛️":
			role = guild.get_role(1048612720288743476)
			await reaction.member.add_roles(role)
		if reaction.emoji.name == "👑":
			role = guild.get_role(1048612844792467507)
			await reaction.member.add_roles(role)
		if reaction.emoji.name == "👸":
			role = guild.get_role(1048612898789920830)
			await reaction.member.add_roles(role)
		if reaction.emoji.name == "🤴":
			role = guild.get_role(1048612934022070363)
			await reaction.member.add_roles(role)
		if reaction.emoji.name == "💡":
			role = guild.get_role(1048612982785065081)
			await reaction.member.add_roles(role)
		if reaction.emoji.name == "💂":
			role = guild.get_role(1048613126637105202)
			await reaction.member.add_roles(role)
@client.event
async def on_raw_reaction_remove(reaction):
	guild = client.get_guild(1045680764261507072)
	member = await guild.fetch_member(reaction.user_id)
	if reaction.message_id == 1047223457877852170:
		if reaction.emoji.name == "👨‍💼":
			role = guild.get_role(1048612594426064936)
			await member.remove_roles(role)
		if reaction.emoji.name == "😆":
			role = guild.get_role(1048612679641735228)
			await member.remove_roles(role)
		if reaction.emoji.name == "🏛️":
			role = guild.get_role(1048612720288743476)
			await member.remove_roles(role)
		if reaction.emoji.name == "👑":
			role = guild.get_role(1048612844792467507)
			await member.remove_roles(role)
		if reaction.emoji.name == "👸":
			role = guild.get_role(1048612898789920830)
			await member.remove_roles(role)
		if reaction.emoji.name == "🤴":
			role = guild.get_role(1048612934022070363)
			await member.remove_roles(role)
		if reaction.emoji.name == "💡":
			role = guild.get_role(1048612982785065081)
			await member.remove_roles(role)
		if reaction.emoji.name == "💂":
			role = guild.get_role(1048613126637105202)
			await member.remove_roles(role)

client.run(os.environ["DISCORD_TOKEN"])

