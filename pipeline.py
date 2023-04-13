import sys
import anyio
import dagger


async def pipeline():
    async with dagger.Connection(
        dagger.Config(log_output=sys.stderr)
    ) as client:
        src = client.host().directory(".")
        python = (
            client.container()
            .from_("python:3.10")
            .with_mounted_directory("/src", src)
            .with_workdir("/src")
            .with_exec(["pip3", "install", "poetry"])
            .with_exec(["poetry", "config", "virtualenvs.create", "false"])
            .with_exec(["poetry", "install", "--without", "test,pipeline,dev"])
            .with_exec(
                [
                    "python3",
                    "mix.py",
                    "--name",
                    "Donde te agarro el cumbion",
                ]
            )
        )

        await python.exit_code()

    print("Cash run succeeded!")


if __name__ == "__main__":
    anyio.run(pipeline)
