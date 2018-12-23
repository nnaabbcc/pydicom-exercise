from pynetdicom3 import AE

ae = AE(ae_title="MY_ECHO_SCU_TEST")
ae.add_requested_context('1.2.840.10008.1.1')

assoc = ae.associate("127.0.0.1", 104)
print(assoc)

if assoc.is_established:
    status = assoc.send_c_echo()
    print(status)

    assoc.release()

