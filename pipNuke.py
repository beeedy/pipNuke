import subprocess
import os

def nuke(name, wait_for_finish=True):
	test = subprocess.Popen(["pip", "freeze"], stdout=subprocess.PIPE).communicate()[0]
	packages = [a.split("==")[0] for a in test.split("\n")][:-1]

	processes = []

	for package in packages:
		if name in package:
			print "Removing {}".format(package)
			processes.append(subprocess.Popen(["sudo", "-H", "pip", "uninstall", package, "-y"], stdout=subprocess.PIPE))

	if wait_for_finish:
		print "waiting for processes to finish..."
		[process.wait() for process in processes]


def main():
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument("string", help="Python packages with this substring will be uninstalled")
	args = parser.parse_args()

	if os.getuid() != 0:
		print "Please rerun with sudo"
		return

	if len(args.string) <= 3:
		print "The substring needs to be longer than 3 characters for your own safety"
		return

	while True:
		print "Remove packages with '{}' as a substring? (Y/n)".format(args.string)
		ans = raw_input().upper()
		if ans != "Y" and ans != "N":
			print "Unable to interpret answer"
			continue
		break

	if ans == "N":
		print "Aborting"
		return

	nuke(args.string)


if __name__ == "__main__":
	main()