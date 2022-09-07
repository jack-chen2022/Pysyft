# syft absolute
import syft as sy
from syft.lib.python.string import String


def test_string_serde() -> None:
    syft_string = String("Hello OpenMined")

    serialized = sy.serialize(syft_string)

    deserialized = sy.deserialize(serialized)

    assert isinstance(deserialized, String)
    assert deserialized.id == syft_string.id


def test_string_send(client: sy.VirtualMachineClient) -> None:
    syft_string = String("Hello OpenMined!")
    ptr = syft_string.send(client)

    # Check pointer type
    assert ptr.__class__.__name__ == "StringPointer"

    # Check that we can get back the object
    res = ptr.get()
    assert res == syft_string
